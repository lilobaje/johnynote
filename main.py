from website import create_app
app = create_app()

if __name__ == '__main__':
    app.run(debug=True) #turn of when running in production

    