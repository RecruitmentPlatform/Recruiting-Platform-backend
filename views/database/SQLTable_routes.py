from flask import request, jsonify
from models.classes.SQLTable import SQLTable

protected_tables = {'college','company','degree','employment_type','ethnicity','gender','gender_pronoun','industry','job_category','job_position','lanaguage','skill'}

def get(table_name,argument_dict):
    results = SQLTable.get(tableName = table_name, argument_dict = argument_dict)
    if results:
        return jsonify(
            status = 200,
            table_name = results)
    return jsonify(
            status=404,
            message=f"No {table_name} in database.")

def delete(table_name, id):
    if table_name in protected_tables:
        return jsonify(
                    status=404,
                    message="Can't delete protected table."
               )
    result = SQLTable.get(tableName = table_name, criteria = "id", criteria_value = id)
    if result:
        SQLTable.delete(table_name,id)
        jsonify(
            status=200,
            message="Row deleted"
        )
        return jsonify(
                    status=404,
                    message="No matching row to delete."
               )
