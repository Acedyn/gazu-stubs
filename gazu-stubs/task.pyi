from typing import Literal, TypeAlias, TypedDict

from gazu.project import ProjectDict

from .client import KitsuClient, default_client

class TaskDict(TypedDict):
    name: str
    description: str | None
    priority: int
    duration: float
    estimation: float
    completion_rate: int
    retake_count: int
    sort_order: int
    start_date: None
    due_date: None
    real_start_date: None
    end_date: None
    done_date: None
    last_comment_date: None
    nb_assets_ready: int
    data: None
    shotgun_id: None
    last_preview_file_id: str | None
    project_id: str
    task_type_id: str
    task_status_id: str
    entity_id: str
    assigner_id: str
    assignees: list[str]
    id: str
    created_at: str
    updated_at: str
    type: Literal["Task"]
    # entity:
    # entity_type: EntityType
    is_subscribed: bool
    # persons: list[PersonDict]
    # project: Project
    task_status: TaskStatusDict
    # task_type: TaskType
    # assigner: PersonDict
    # sequence: Sequence

class TaskStatusDict(TypedDict):
    name: str
    archived: bool
    short_name: str
    description: str | None
    color: str
    priority: int
    is_done: bool
    is_artist_allowed: bool
    is_client_allowed: bool
    is_retake: bool
    is_feedback_request: bool
    is_default: bool
    shotgun_id: str | None
    for_concept: bool
    id: str
    created_at: str
    updated_at: str
    type: Literal["TaskStatus"]

class TaskTypeDict(TypedDict):
    name: str
    short_name: str
    description: str | None
    color: str
    priority: int
    for_entity: Literal["Shot"]
    allow_timelog: bool
    archived: bool
    shotgun_id: str | None
    department_id: str
    id: str
    created_at: str
    updated_at: str
    type: Literal["TaskType"]

EntityType: TypeAlias = Literal["Asset", "Shot", "Sequence", "Edit"]

def get_task(task_id: str, client: KitsuClient = default_client) -> TaskDict: ...
def get_task_status(
    task_status_id: str, client: KitsuClient = default_client
) -> TaskStatusDict: ...
def get_task_type(
    task_type_id: str, client: KitsuClient = default_client
) -> TaskTypeDict: ...
def all_task_statuses_for_project(
    project: str | ProjectDict, client: KitsuClient = default_client
) -> list[TaskStatusDict]: ...
def get_task_status_by_name(
    name: str, client: KitsuClient = default_client
) -> TaskStatusDict | None: ...
def get_task_type_by_name(
    task_type_name: str,
    for_entity: EntityType | None = None,
    department: str | None = None,
    client: KitsuClient = default_client,
) -> TaskTypeDict | None: ...
def all_task_types_for_project(
    project: ProjectDict | str, client: KitsuClient = default_client
) -> list[TaskTypeDict]: ...
