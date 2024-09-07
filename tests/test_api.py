# -*- coding: utf-8 -*-

from aws_code_artifact_python_example import api


def test():
    _ = api


if __name__ == "__main__":
    from aws_code_artifact_python_example.tests import run_cov_test

    run_cov_test(__file__, "aws_code_artifact_python_example.api", preview=False)
