"""Management commands to populate candidate profiles."""

import logging
from typing import Any
from tqdm import tqdm
from django.core.management.base import BaseCommand

from candidate.tests import ProfileFactory

logger = logging.getLogger(__name__)


class Command(BaseCommand):
    """Django management command to populate profiles data using profile factory."""

    help = "Populate candidate profiles data using Factory."

    def handle(self, *args: Any, **options: Any) -> str | None:
        logger.info("Script to create profile data started!!!")

        # Prompt the user for the number of profiles to create, handling invalid inputs
        while True:
            try:
                num_profiles = int(input("Enter the number of profiles to create: "))
                break
            except ValueError:
                logger.error("Invalid input. Please enter a valid integer.")

        # Use tqdm to display a progress bar while creating profiles.
        profiles = tqdm(ProfileFactory.create_batch(size=num_profiles))

        logger.info(f"{len(profiles)} profiles created successfully!!!")

        logger.info("Script to create profile data successfully completed!!!")
