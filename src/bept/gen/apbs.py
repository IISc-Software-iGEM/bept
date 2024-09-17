import warnings

from bept.gen.interface import InputApp, input_fileload


def apbs_gen(input_file_path: str):
    """
    Interactive APBS input file generator.
    Args:
        input_file_path: The path to the input file
    """
    data = input_fileload(input_file_path)
    app = InputApp(data, input_file_path)
    app.run()

    for i in InputApp.ion:
        if i.count("") == 2 or i.count("") == 1:
            warnings.warn(
                "All the parameters for ion"
                + str(InputApp.ion.index(i) + 1)
                + " are not provided, and it will be ignored in the calculation"
            )
