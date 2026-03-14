import pytest
from frontend.src.pages.Dashboard import Dashboard

@pytest.fixture
def dummy_set_screen():
    def set_screen(screen_name):
        pass
    return set_screen

@pytest.fixture
def dummy_set_current_run_id():
    def set_current_run_id(run_id):
        pass
    return set_current_run_id

@pytest.fixture
def valid_stats():
    return {
        'successRate': 75,
        'totalFixes': 10,
        'avgFixTime': 300,
        'byDay': {},
        'byBugType': {},
        'thisMonth': 50,
        'lastMonth': 45,
        'totalRuns': 20
    }

@pytest.fixture
def empty_stats():
    return {
        'successRate': 0,
        'totalFixes': 0,
        'avgFixTime': 0,
        'byDay': {},
        'byBugType': {},
        'thisMonth': 0,
        'lastMonth': 0,
        'totalRuns': 0
    }

@pytest.fixture
def valid_runs():
    return [{'id': 1, 'status': 'completed'}, {'id': 2, 'status': 'failed'}]

@pytest.fixture
def mock_fetch_data(mocker, valid_stats, valid_runs):
    return mocker.patch('frontend.src.pages.Dashboard.fetchData', return_value=(valid_stats, valid_runs))

async def test_dashboard_renders_correctly_with_valid_data(dummy_set_screen, dummy_set_current_run_id, mocker, valid_stats, valid_runs):
    """
    Test Dashboard component renders correctly when valid stats and runs are provided.
    """
    mocker.patch('frontend.src.pages.Dashboard.getStats', return_value=valid_stats)
    mocker.patch('frontend.src.pages.Dashboard.getRuns', return_value=valid_runs)

    component = Dashboard(setScreen=dummy_set_screen, setCurrentRunId=dummy_set_current_run_id)
    component.componentDidMount()

    assert component.state['stats'] == valid_stats
    assert component.state['runs'] == valid_runs
    assert component.state['apiConnected'] == True

async def test_dashboard_handles_api_failure(dummy_set_screen, dummy_set_current_run_id, mocker, empty_stats):
    """
    Test Dashboard component gracefully handles API failure by using EMPTY_STATS.
    """
    mocker.patch('frontend.src.pages.Dashboard.getStats', side_effect=Exception('API unreachable'))
    mocker.patch('frontend.src.pages.Dashboard.getRuns', side_effect=Exception('API unreachable'))

    component = Dashboard(setScreen=dummy_set_screen, setCurrentRunId=dummy_set_current_run_id)
    component.componentDidMount()

    assert component.state['stats'] == empty_stats
    assert component.state['runs'] == []
    assert component.state['apiConnected'] == False
