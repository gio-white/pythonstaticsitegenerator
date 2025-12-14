import os
import shutil
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def static_to_public():
    logging.info("Starting static_to_public")
    if os.path.exists("./public"):
        logging.info("Removing existing ./public directory")
        shutil.rmtree("./public")
    logging.info("Creating ./public directory")
    os.mkdir("./public")
    recursive_copy("./static", "./public")
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

static_to_public()