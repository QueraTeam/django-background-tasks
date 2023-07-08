__version__ = "1.2.5"


def background(*arg, **kw):
    from background_task.tasks import tasks

    return tasks.background(*arg, **kw)
