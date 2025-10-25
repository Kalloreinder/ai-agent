from google.genai import types
import functions

FUNCTIONS = {
    "get_file_content": functions.get_file_content,
    "get_files_info": functions.get_files_info,
    "run_python_file": functions.run_python_file,
    "write_file": functions.write_file,
}

def call_function(function_call_part, verbose=False):

    if verbose:
        print(f"Calling function: {function_call_part.name}({function_call_part.args})")
    else:
        print(f"- Calling function: {function_call_part.name}")

    kwargs = function_call_part.args.copy()
    kwargs["working_directory"] = "./calculator"

    func = FUNCTIONS.get(function_call_part.name)

    if func == None:
        return types.Content(
            role="tool",
            parts=[
                types.Part.from_function_response(
                    name=function_call_part.name,
                    response={"error": f"Unknown function: {function_call_part.name}"}
                )
            ]
        )
    
    function_result = func(**kwargs)

    return types.Content(
        role="tool",
        parts=[
            types.Part.from_function_response(
                name=function_call_part.name,
                response={"result": function_result}
            )
        ]
    )

    return 0