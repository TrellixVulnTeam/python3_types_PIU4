from django.db import migrations
from typing import Any

def migrate_org_data(apps: Any, schema_editor: Any) -> None: ...
def clean_org_data(apps: Any, schema_editor: Any) -> None: ...

class Migration(migrations.Migration):
    dependencies: Any = ...
    operations: Any = ...
