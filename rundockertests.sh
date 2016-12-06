#!/bin/bash
# Run docker tests on your local machine

PLUGIN_NAME="geoserverexplorer"
# One of master_2, master, release
TARGET_VERSION=master

if [ $TARGET_VERSION = 'master' ]; then
    PIP_EXECUTABLE=pip3
else
    PIP_EXECUTABLE=pip
fi

docker-compose down -v
docker-compose up -d
sleep 10

DOCKER_RUN_COMMAND="docker-compose exec qgis-testing-environment sh -c"

# Setup
$DOCKER_RUN_COMMAND "qgis_setup.sh $PLUGIN_NAME"
$DOCKER_RUN_COMMAND "$PIP_EXECUTABLE install paver"
$DOCKER_RUN_COMMAND "cd /tests_directory && paver setup && paver package --tests"

# Run the tests
$DOCKER_RUN_COMMAND "qgis_testrunner.sh geoserverexplorer.test.catalogtests"
$DOCKER_RUN_COMMAND "qgis_testrunner.sh geoserverexplorer.test.deletetests"
$DOCKER_RUN_COMMAND "qgis_testrunner.sh geoserverexplorer.test.guitests"
$DOCKER_RUN_COMMAND "qgis_testrunner.sh geoserverexplorer.test.dragdroptests"
$DOCKER_RUN_COMMAND "qgis_testrunner.sh geoserverexplorer.test.pkicatalogtests"
$DOCKER_RUN_COMMAND "qgis_testrunner.sh geoserverexplorer.test.pkideletetests"
$DOCKER_RUN_COMMAND "qgis_testrunner.sh geoserverexplorer.test.pkiguitests"
$DOCKER_RUN_COMMAND "qgis_testrunner.sh geoserverexplorer.test.pkidragdroptests"
$DOCKER_RUN_COMMAND "qgis_testrunner.sh geoserverexplorer.test.pkiowstests"
