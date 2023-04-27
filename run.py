from app.app import create_app

# took this line from the if-statement below (before app.run())
app = create_app()

if __name__ == "__main__":
    app.run()
