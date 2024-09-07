# -*- coding: utf-8 -*-

import subprocess

from .paths import (
    bin_pytest,
    dir_tests,
    dir_htmlcov,
    dir_project_root,
    temp_current_dir,
)
from .pyproject import pyproject
from .runtime import IS_CI
from .git import (
    GIT_BRANCH_NAME,
    IS_MASTER_BRANCH,
    IS_DEV_BRANCH,
    IS_FEATURE_BRANCH,
)
from .logger import logger
from .emoji import Emoji
from .tests_rule import do_we_run_unit_test


@logger.block(
    msg="Run Unit Test",
    start_emoji=Emoji.test,
    end_emoji=Emoji.test,
    pipe=Emoji.test,
)
def run_unit_test(
    check: bool = True,
):
    if check:
        if (
            do_we_run_unit_test(
                is_ci_runtime=IS_CI,
                branch_name=GIT_BRANCH_NAME,
                is_master_branch=IS_MASTER_BRANCH,
                is_dev_branch=IS_DEV_BRANCH,
                is_feature_branch=IS_FEATURE_BRANCH,
            )
            is False
        ):
            return

    args = [
        f"{bin_pytest}",
        f"{dir_tests}",
        "-s",
    ]
    with temp_current_dir(
        dir_project_root
    ):  # ensure current dir is the project root
        subprocess.run(args, check=True)


@logger.block(
    msg="Run Code Coverage Test",
    start_emoji=Emoji.test,
    end_emoji=Emoji.test,
    pipe=Emoji.test,
)
def run_cov_test(
    check: bool = True,
):
    if check:
        if (
            do_we_run_unit_test(
                is_ci_runtime=IS_CI,
                branch_name=GIT_BRANCH_NAME,
                is_master_branch=IS_MASTER_BRANCH,
                is_dev_branch=IS_DEV_BRANCH,
                is_feature_branch=IS_FEATURE_BRANCH,
            )
            is False
        ):
            return

    args = [
        f"{bin_pytest}",
        f"{dir_tests}",
        "-s",
        f"--cov={pyproject.package_name}",
        "--cov-report",
        "term-missing",
        "--cov-report",
        f"html:{dir_htmlcov}",
    ]
    with temp_current_dir(
        dir_project_root
    ):  # ensure current dir is the project root
        subprocess.run(args, check=True)
