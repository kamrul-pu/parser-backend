"""Management command to populate dummy open jobs."""

import logging
from typing import Any
from tqdm import tqdm
from django.core.management.base import BaseCommand

from recruitment.tests import OpenJobsFactory

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Django management command to populate open jobs datausing factory."""

    help = "Populate open jobs data using Factory."

    def handle(self, *args: Any, **options: Any) -> str | None:
        logger.info("Script to create jobs data started!!!")

        # Prompt the user for the number of jobs to create, handling invalid inputs
        while True:
            try:
                num_jobs = int(input("Enter the number of jobs to create: "))
                break
            except ValueError:
                logger.error("Invalid input. Please enter a valid integer.")

        # Use tqdm to display a progress bar while creating jobs.
        jobs = tqdm(OpenJobsFactory.create_batch(size=num_jobs))

        logger.info(f"{len(jobs)} Jobs created successfully!!!")

        logger.info("Script to create jobs data successfully completed!!!")
