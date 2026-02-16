"""
Module entry point
"""

from base_toshi_api.schema.custom import SmsFile, StrongMotionStation
from base_toshi_api.schema.custom.aggregate_inversion_solution import (
    AggregateInversionSolution,
    CreateAggregateInversionSolution,
)
from base_toshi_api.schema.custom.automation_task import AutomationTask, CreateAutomationTask, UpdateAutomationTask
from base_toshi_api.schema.custom.general_task import GeneralTask
from base_toshi_api.schema.custom.inversion_solution import CreateInversionSolution, InversionSolution
from base_toshi_api.schema.custom.inversion_solution_nrml import CreateInversionSolutionNrml, InversionSolutionNrml
from base_toshi_api.schema.custom.openquake_hazard_config import CreateOpenquakeHazardConfig, OpenquakeHazardConfig
from base_toshi_api.schema.custom.openquake_hazard_solution import (
    CreateOpenquakeHazardSolution,
    OpenquakeHazardSolution,
)
from base_toshi_api.schema.custom.openquake_hazard_task import CreateOpenquakeHazardTask, OpenquakeHazardTask
from base_toshi_api.schema.custom.rupture_generation_task import RuptureGenerationTask, RuptureGenerationTaskConnection
from base_toshi_api.schema.custom.rupture_set import CreateRuptureSet, RuptureSet
from base_toshi_api.schema.custom.scaled_inversion_solution import (
    CreateScaledInversionSolution,
    ScaledInversionSolution,
)
from base_toshi_api.schema.custom.time_dependent_inversion_solution import (
    CreateTimeDependentInversionSolution,
    TimeDependentInversionSolution,
)
from base_toshi_api.schema.event import EventResult, EventState
from base_toshi_api.schema.file import CreateFile, File, FileConnection
from base_toshi_api.schema.file_relation import FileRelation
from base_toshi_api.schema.schema import root_schema
from base_toshi_api.schema.search_manager import SearchManager
from base_toshi_api.schema.table import Table
from base_toshi_api.schema.task_task_relation import TaskTaskRelation
from base_toshi_api.schema.thing import Thing, ThingConnection
