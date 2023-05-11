from lib.config import CONFIG


def build_app():
    import connexion as connexion

    DEBUG_MODE = (CONFIG.ENVIRONMENT != 'production')
    app = connexion.App(__name__, specification_dir='lib/', debug=DEBUG_MODE)

    app.add_api('api/api_spec.yaml', base_path='/',
                validate_responses=DEBUG_MODE, options={"swagger_ui": True})

    flask_app = app.app

    # activate config
    flask_app.config.from_object(CONFIG)

    return flask_app


app = build_app()

# if __name__ == '__main__':
#    app.run(port=8080)
