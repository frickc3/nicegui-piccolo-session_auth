import os
import argparse
import uvicorn
from app import frontend
from fastapi import FastAPI
from icecream import install

install()
ic.disable()

fapp = FastAPI()
frontend.init(fapp)

if __name__ == "__main__":
    import uvicorn

    parser = argparse.ArgumentParser()

    parser.add_argument("-p", "--port", help="http Port",
                         default=8080, action="store")

    parser.add_argument("-v", "--verbose", help="Print detailed debugging information.",
                        action="store_true")

    parser.add_argument("-r", "--reload", help="Reload on changes, default False.",
                        action="store_true", default=False)

    parser.add_argument("-d", "--debug", help="Print debugging information.",
                        action="store_true", default=False)

    args = parser.parse_args()
    log_level = "info"
    if args.verbose:
        log_level = "debug"
    port = int(args.port)

    if args.debug:
        ic.enable()
        os.environ['IC_DEBUG'] = 'True'
    ic(args)

    uvicorn.run("main:fapp", host="127.0.0.1", port=port, reload=args.reload,
                log_level=log_level)