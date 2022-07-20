import ast
import sys
import os
import re


def count_start_spaces(s):
    return len(s) - len(s.lstrip())


def count_end_spaces(s):
    return len(s) - len(s.rstrip())


def sort_func(e):
    return e['lineno']


def check_file(filepath):
    file = open(filepath, 'r')
    file_read = file.read()
    tree = ast.parse(file_read)
    errors_list = []
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            function_name = node.name
            # check whether the function's name is written in camel_case
            if re.match(r'_?_?[a-z]+_?[a-z]*', function_name) is None:
                errors_list.append({'filepath': filepath,
                                    'lineno': node.lineno,
                                    'message': 'S009 Function name function_name should be written in snake_case'})
            for arg in node.args.args:
                if re.match(r'_?_?[a-z]+_?[a-z]*', arg.arg) is None:
                    errors_list.append({'filepath': filepath,
                                        'lineno': node.lineno,
                                        'message': 'S010 Argument name arg_name should be written in snake_case'})

            for arg in node.args.defaults:
                if isinstance(arg, ast.List):
                    errors_list.append({'filepath': filepath,
                                        'lineno': node.lineno,
                                        'message': 'S012 The default argument value is mutable'})

            for expr in node.body:
                if isinstance(expr, ast.Assign):
                    for target in expr.targets:
                        if isinstance(target, ast.Name) and re.match(r'_?_?[a-z]+_?[a-z]*', target.id) is None:
                            errors_list.append({'filepath': filepath,
                                                'lineno': target.lineno,
                                                'message': 'S011 Variable var_name should be written in snake_case'})

        if isinstance(node, ast.Param):
            if re.match(r'[A-Z][a-z]+[A-Z]?[a-z]*', node.name) is None:
                errors_list.append({'filepath': filepath,
                                    'lineno': node.lineno,
                                    'message': "S008 Class name class_name should be written in CamelCase"})
        if isinstance(node, ast.ClassDef):
            if re.match(r'[A-Z][a-z]+[A-Z]?[a-z]*', node.name) is None:
                errors_list.append({'filepath': filepath,
                                    'lineno': node.lineno,
                                    'message': "S008 Class name class_name should be written in CamelCase"})

    lines = file_read.splitlines()
    line_counter = 1
    empty_line_counter = 0
    for line in lines:
        splited_line = line.split("#")
        if len(line) > 79:
            errors_list.append({'filepath': filepath,
                                'lineno': line_counter,
                                'message': "S001 Too long"})
        if count_start_spaces(line) % 4 != 0 and not line.startswith("#"):
            errors_list.append({'filepath': filepath,
                                'lineno': line_counter,
                                'message': "S002 Indentation is not a multiple of four"})
        if not line.startswith("#") and splited_line[0].rstrip().endswith(";"):
            errors_list.append({'filepath': filepath,
                                'lineno': line_counter,
                                'message': "S003 Unnecessary semicolon"})
        if len(splited_line) > 1 and len(splited_line[0]) > 0 and count_end_spaces(splited_line[0]) < 2:
            errors_list.append({'filepath': filepath,
                                'lineno': line_counter,
                                'message': "S004 At least two spaces required before inline comments"})
        if len(splited_line) > 1 and splited_line[1].lower().find("todo") > -1:
            errors_list.append({'filepath': filepath,
                                'lineno': line_counter,
                                'message': "S005 TODO found"})
        if len(line) == 0:
            empty_line_counter += 1
        if len(line) > 0:
            if empty_line_counter == 3:
                errors_list.append({'filepath': filepath,
                                    'lineno': line_counter,
                                    'message': "S006 More than two blank lines used before this line"})
            empty_line_counter = 0
        if line.startswith("class") and re.match(r'^class [a-zA-Z]+', line) is None:
            errors_list.append({'filepath': filepath,
                                'lineno': line_counter,
                                'message': "S007 Too many spaces after 'class'"})
        if line.lstrip().startswith("def") and re.match(r'def _?_?[a-zA-z]+', line.lstrip()) is None:
            errors_list.append({'filepath': filepath,
                                'lineno': line_counter,
                                'message': "S007 Too many spaces after 'def'"})
        line_counter += 1
    file.close()
    errors_list.sort(key=sort_func)
    for error in errors_list:
        print("{}: Line {}: {}".format(error['filepath'], error['lineno'], error['message']))


filelist_to_check = []
args = sys.argv

directory_or_file = args[1]
if os.path.isdir(directory_or_file):
    for entry in os.listdir(directory_or_file):
        if os.path.isfile(os.path.join(directory_or_file, entry)) and entry.endswith(".py"):
            filelist_to_check.append(os.path.join(directory_or_file, entry))
elif os.path.isfile(directory_or_file):
    filelist_to_check.append(directory_or_file)
else:
    print("Incorrect dir or file argument")

filelist_to_check.sort()
for file in filelist_to_check:
    check_file(file)
