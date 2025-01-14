# (generated with --quick)

from typing import Any

FromParams: Any
Model: Any
SummaryWriter: Any
logger: logging.Logger
logging: module
os: module
torch: Any

class TensorboardWriter(Any):
    __doc__: str
    _histogram_interval: Any
    _should_log_learning_rate: Any
    _should_log_parameter_statistics: Any
    _summary_interval: Any
    _train_log: Any
    _validation_log: Any
    def __init__(self, get_batch_num_total, serialization_dir = ..., summary_interval = ..., histogram_interval = ..., should_log_parameter_statistics = ..., should_log_learning_rate = ...) -> None: ...
    def _get_batch_num_total(self) -> Any: ...
    @staticmethod
    def _item(value) -> Any: ...
    def add_train_histogram(self, name, values) -> None: ...
    def add_train_scalar(self, name, value, timestep = ...) -> None: ...
    def add_validation_scalar(self, name, value, timestep = ...) -> None: ...
    def close(self) -> None: ...
    def enable_activation_logging(self, model) -> None: ...
    def log_activation_histogram(self, outputs, log_prefix) -> None: ...
    def log_histograms(self, model, histogram_parameters) -> None: ...
    def log_learning_rates(self, model, optimizer) -> None: ...
    def log_metrics(self, train_metrics, val_metrics = ..., epoch = ..., log_to_console = ...) -> None: ...
    def log_parameter_and_gradient_statistics(self, model, batch_grad_norm) -> None: ...
    def should_log_histograms_this_batch(self) -> Any: ...
    def should_log_this_batch(self) -> Any: ...
