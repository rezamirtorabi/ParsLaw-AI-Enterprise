from pars_law.core.config import Settings

def test_default_settings():
    settings = Settings()
    assert settings.app_name == "ParsLaw AI Enterprise"
    assert settings.database_url.startswith("sqlite:///")
