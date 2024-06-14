from django.shortcuts import render
from .models import Event, Dependency, Resource, Assignment
from django.http import JsonResponse
from django.views.decorators.http import require_GET
from django.views.decorators.csrf import csrf_exempt

import json


def index(request):
    return render(request, 'index.html')


@require_GET
def load(request):
    try:
        events = list(Event.objects.all().values())
        dependencies = list(Dependency.objects.all().values())
        assignments = list(Assignment.objects.all().values())
        resources = list(Resource.objects.all().values())

        for dependency in dependencies:
            dependency['fromEvent'] = dependency.pop('fromEvent_id')
            dependency['toEvent'] = dependency.pop('toEvent_id')

        for assignment in assignments:
            assignment['eventId'] = assignment.pop('eventId_id')
            assignment['resourceId'] = assignment.pop('resourceId_id')

        response_data = {
            "success": True,
            "events": {
                "rows": events,
            },
            "dependencies": {
                "rows": dependencies,
            },
            "assignments": {
                "rows": assignments,
            },
            "resources": {
                "rows": resources,
            },
        }
        return JsonResponse(response_data)

    except Exception as e:
        return JsonResponse({
            "success": False,
            "error": str(e)
        }, status=500)


def create_operation(added, table):
    record_mapping = []
    for record in added:
        phantom_id = record.pop('$PhantomId', None)
        new_record = None

        if table == 'events':
            new_record = Event.objects.create(**record)

        if table == 'dependencies':
            record['fromEvent_id'] = record.pop('from')
            record['toEvent_id'] = record.pop('to')
            new_record = Dependency.objects.create(**record)

        if table == 'resources':
            new_record = Resource.objects.create(**record)

        if table == 'assignments':
            record['eventId_id'] = record.pop('eventId')
            record['resourceId_id'] = record.pop('resourceId')
            new_record = Assignment.objects.create(**record)

        if new_record:
            record_mapping.append({'$PhantomId': phantom_id, 'id': new_record.id})
    return record_mapping


def update_operation(updated, table):
    for record in updated:
        if table == 'events':
            Event.objects.filter(id=record['id']).update(**record)

        if table == 'dependencies':
            Dependency.objects.filter(id=record['id']).update(**record)

        if table == 'resources':
            Resource.objects.filter(id=record['id']).update(**record)

        if table == 'assignments':
            Assignment.objects.filter(id=record['id']).update(**record)


def delete_operation(deleted, table):
    for record in deleted:
        if table == 'events':
            Event.objects.filter(id=record['id']).delete()

        if table == 'dependencies':
            Dependency.objects.filter(id=record['id']).delete()

        if table == 'resources':
            Resource.objects.filter(id=record['id']).delete()

        if table == 'assignments':
            Assignment.objects.filter(id=record['id']).delete()


def apply_table_changes(table, changes):
    rows = None
    if 'added' in changes:
        rows = create_operation(changes['added'], table)
    if 'updated' in changes:
        update_operation(changes['updated'], table)
    if 'removed' in changes:
        delete_operation(changes['removed'], table)
    return rows


@csrf_exempt
def sync(request):
    if request.method == 'POST':
        data = json.loads(request.body.decode('utf-8'))
        request_id = data.get('requestId')
        events = data.get('events')
        dependencies = data.get('dependencies')
        resources = data.get('resources')
        assignments = data.get('assignments')

        event_mapping = {}

        try:
            response = {'requestId': request_id, 'success': True}
            if events:
                rows = apply_table_changes("events", events)
                if rows:
                    if 'added' in events:
                        for row in rows:
                            event_mapping[row['$PhantomId']] = row['id']
                    response['events'] = {'rows': rows}

            if dependencies:
                rows = apply_table_changes("dependencies", dependencies)
                if rows:
                    response['dependencies'] = {'rows': rows}

            if resources:
                rows = apply_table_changes("resources", dependencies)
                if rows:
                    response['resources'] = {'rows': rows}

            if assignments:
                if events and 'added' in events:
                    for assignment in assignments.get('added', []):
                        assignment['eventId'] = event_mapping.get(assignment['eventId'])
                rows = apply_table_changes("assignments", assignments)
                if rows:
                    response['assignments'] = {'rows': rows}

            return JsonResponse(response)
        except Exception as e:
            print(e)
    return JsonResponse(
        {'success': False, 'message': 'There was an error syncing the data changes.'})
