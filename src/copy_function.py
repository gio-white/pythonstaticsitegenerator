import os
import shutil
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def static_to_public():
    logging.info("Starting static_to_public")
    if os.path.exists("./docs"):
        logging.info("Removing existing ./docs directory")
        shutil.rmtree("./docs")
    logging.info("Creating ./docs directory")
    os.mkdir("./docs")
    recursive_copy("./static", "./docs")
    logging.info("Finished static_to_public")


def recursive_copy(src_path, dest_path):
    logging.info("Entering recursive_copy: %s -> %s", src_path, dest_path)
    for item in os.listdir(src_path):
        copy_from = os.path.join(src_path, item)
        copy_to = os.path.join(dest_path, item)
        if not os.path.isfile(copy_from):
            if not os.path.exists(copy_to):
                os.mkdir(copy_to)
                logging.info("Creating directory: %s", copy_to)
            recursive_copy(copy_from, copy_to)
        else:
            shutil.copy(copy_from, copy_to)
            logging.info("Copying file: %s -> %s", copy_from, copy_to)
    logging.info("Exiting recursive_copy: %s", src_path)