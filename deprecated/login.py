from flask import Blueprint
from flask import render_template, request, redirect
from cloudmesh.config.cm_keys import cm_keys
import cloudmesh


from cloudmesh.util.logger import LOGGER

log = LOGGER(__file__)


login_module = Blueprint('login_module', __name__)

#
# ROUTE: login
#


@login_module.route('/abc/', methods=['GET', 'POST'])
def nothing():
    pass
