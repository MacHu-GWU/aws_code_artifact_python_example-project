# -*- coding: utf-8 -*-

if __name__ == "__main__":
    from aws_code_artifact_python_example.tests import run_cov_test

    run_cov_test(__file__, "aws_code_artifact_python_example", is_folder=True, preview=False)
