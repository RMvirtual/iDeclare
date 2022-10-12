from rules_python.python.runfiles import runfiles


def load_path(src_path: str):
    """From the bazel workspace, loads a file from the subdirectory.

    Must be exported as a file in bazel and be passed as a data item in
    the build file of the library that uses this function.
    """
    r = runfiles.Create()
    location = r.Rlocation("CustomsAPI/" + src_path)

    if not location:
        raise FileNotFoundError(
            src_path + " is not accessible as a runfile or does not exist.")

    return location
