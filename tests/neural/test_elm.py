from pyridge.experiment.check import check_algorithm


def test_elm():
    hyperparameter_elm = {'activation': ['sigmoid'],
                          'reg': [10 ** i for i in range(-1, 2)],
                          'hidden_neurons': [10]}
    value_dict = check_algorithm(folder='data',
                                 dataset='iris',
                                 algorithm='ELM',
                                 hyperparameter=hyperparameter_elm,
                                 metric_list=['accuracy', 'rmse'])


def test_elm_regression():
    hyperparameter_elm = {'activation': ['sigmoid'],
                          'reg': [10 ** i for i in range(-1, 2)],
                          'hidden_neurons': [10]}
    value_dict = check_algorithm(folder='data_regression',
                                 dataset='housing',
                                 algorithm='ELM',
                                 hyperparameter=hyperparameter_elm,
                                 metric_list=['rmse'],
                                 classification=False)
