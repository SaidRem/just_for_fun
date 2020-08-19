import logging
import timer


def logger_func(orig_f):
    logging.basicConfig(filename='{}.log'.format(orig_f.__name__),
                        level=logging.INFO)

    def wrapper(*args, **kwargs):
        logging.info(
            'The function ran with args: {}, and kwargs: {}'.format(args,
                                                                    kwargs)
        )
        return orig_f(*args, **kwargs)
    return wrapper
