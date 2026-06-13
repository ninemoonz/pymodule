if __name__ == "__main__":
    dict_sample = [{'log_level': 'NOTICE', 'log_message': 'Connection to server'},
                   {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}]
    for sample in dict_sample:
        print(sample.keys())