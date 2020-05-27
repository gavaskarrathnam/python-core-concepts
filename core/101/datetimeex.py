from datetime import datetime, timedelta
import yaml
import logging


LOG_FORMAT = ('%(levelname) -10s %(asctime)s %(name) -30s %(funcName) '
              '-35s %(lineno) -5d: %(message)s')
logging.basicConfig(level=logging.INFO, format=LOG_FORMAT)
LOGGER = logging.getLogger(__name__)


# get today date
def find_today():
    now = datetime.now()
    #print("now :", now)

    # dd/mm/YY H:M:S
    #dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    #print("full length dt :", dt_string)

    return now.strftime("%d-%m-%Y")


def find_yesterday():
    now = datetime.now()
    #print("timedelta :", timedelta(days=1))

    yesterday = now - timedelta(days=1)
    return yesterday.strftime("%d-%m-%Y")


def build_file(file):
    LOGGER.info("enter into build file")
    with open(file, "rt") as file:
        try:
            data = yaml.safe_load(file)
        except Exception as ex:
            LOGGER.error(ex.message)
            exit()
            
    return {
        "dir1_today": data["dir_1"] + find_today(),
        "dir1_yesterday": data["dir_1"] + find_yesterday(),
        "dir2_today": data["dir_2"] + find_today(),
        "dir2_yesterday": data["dir_2"] + find_yesterday()
    }



#print(find_today())
#print(find_yesterday())
print(build_file("filelist.yaml"))

