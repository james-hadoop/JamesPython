def initLogConfig(logging, full_log_path, log_level='INFO'):
    if not full_log_path or str(full_log_path).__len__() < 1:
        raise Exception

    print("full_log_path=%s" % full_log_path)
    logging.basicConfig(filename=full_log_path,
                        level=log_level,
                        format='%(asctime)s %(filename)s [line:%(lineno)d] %(levelname)8s: %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')


def initPandasSetting(pd):
    pd.set_option('display.max_columns', 1000)

    pd.set_option('display.width', 1000)

    pd.set_option('display.max_colwidth', 1000)

    pd.set_option('display.max_rows', None)
