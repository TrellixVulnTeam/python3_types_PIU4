# (generated with --quick)

from typing import Any, Optional, Tuple

MatchObjTypeError: Any
NotFoundComponentError: Any
v: Any
vc: Any

class AnyJoint:
    _def_op_mode: Any
    _handle: Any
    _id: Any
    def __init__(self, id, handle) -> None: ...
    def get_force(self) -> Any: ...
    def get_matrix(self) -> Any: ...
    def get_position(self) -> Any: ...
    def set_matrix(self, matrix) -> None: ...
    def set_maximum_force(self, force) -> None: ...
    def set_position(self, position) -> None: ...
    def set_target_position(self, target) -> None: ...
    def set_target_velocity(self, target) -> None: ...

class JointWithPositionControl:
    _any_joint: AnyJoint
    def __init__(self, any_joint: AnyJoint) -> None: ...
    def get_force(self) -> Any: ...
    def get_position(self) -> Any: ...
    def set_maximum_force(self, force: float) -> None: ...
    def set_target_position(self, target: float) -> None: ...

class JointWithVelocityControl:
    _any_joint: AnyJoint
    def __init__(self, any_joint: AnyJoint) -> None: ...
    def get_force(self) -> Any: ...
    def get_position(self) -> Any: ...
    def set_maximum_force(self, force: float) -> None: ...
    def set_target_velocity(self, target: float) -> None: ...

class Joints:
    _def_op_mode: Any
    _id: Any
    def __init__(self, id) -> None: ...
    def _get_info_about_joint(self, handle) -> Optional[Tuple[Any, Any, Any, Any]]: ...
    def _get_joint_with_param(self, name, types, mode) -> AnyJoint: ...
    def _get_object_handle(self, name) -> Any: ...
    def passive(self, name: str) -> PassiveJoint: ...
    def spherical(self, name: str) -> SphericalJoint: ...
    def spring(self, name: str) -> SpringJoint: ...
    def with_position_control(self, name: str) -> JointWithPositionControl: ...
    def with_velocity_control(self, name: str) -> JointWithVelocityControl: ...

class PassiveJoint:
    _any_joint: AnyJoint
    def __init__(self, any_joint: AnyJoint) -> None: ...
    def get_position(self) -> Any: ...
    def set_position(self, pos: float) -> None: ...

class SphericalJoint:
    _any_joint: AnyJoint
    def __init__(self, any_joint: AnyJoint) -> None: ...
    def get_matrix(self) -> Any: ...
    def set_matrix(self, matrix) -> None: ...

class SpringJoint:
    _any_joint: AnyJoint
    def __init__(self, any_joint: AnyJoint) -> None: ...
    def get_force(self) -> Any: ...
    def get_position(self) -> Any: ...
    def set_maximum_force(self, force: float) -> None: ...
    def set_target_position(self, target: float) -> None: ...
    def set_target_velocity(self, target: float) -> None: ...
