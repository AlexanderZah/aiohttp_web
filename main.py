from app.web.app import Application, run_app
import logging

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)



if __name__ == '__main__':
    run_app()
