from PyQt5.QtGui import QPainter as QPainter
from PyQt5.QtWidgets import QGraphicsEffect
from typing import Any

class OpacityEffect(QGraphicsEffect):
    opacity: Any = ...
    def __init__(self, opacity: float=...) -> None: ...
    def draw(self, painter: QPainter) -> None: ...
