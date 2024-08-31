import logging
from django.conf import settings
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.cron import CronTrigger
from django_apscheduler.jobstores import DjangoJobStore, register_events
from .services import run_payment_notification
import sys

logger = logging.getLogger(__name__)


def startScheduler():
    if settings.TESTING:
        return
    logger.info('Starting Scheduler')
    scheduler = BackgroundScheduler()
    scheduler.add_jobstore(DjangoJobStore(), 'default')
    scheduler.add_job(
        run_payment_notification,
        trigger=CronTrigger(hour='8', minute='0'),
        id='due_payment_notification',
        max_instances=1,
        replace_existing=True
    )
    register_events(scheduler)
    scheduler.start()
    logger.info("Schedular Started & Registered")
