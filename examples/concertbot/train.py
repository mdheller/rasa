import asyncio

from rasa_core import train, utils

import logging

logger = logging.getLogger(__name__)


async def train_dialogue(domain_file='domain.yml',
                         stories_file='data/stories.md',
                         model_path='models/dialogue',
                         policy_config='policy_config.yml'):
    return await train.train_dialogue_model(domain_file=domain_file,
                                            stories_file=stories_file,
                                            output_path=model_path,
                                            policy_config=policy_config,
                                            kwargs={'augmentation_factor': 50,
                                                    'validation_split': 0.2}
                                            )


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(train_dialogue())

    utils.configure_colored_logging(loglevel="INFO")
    logger.info("This example does not include NLU data."
                "Please specify the desired intent with a preceding '/', e.g."
                "'/greet' .")
