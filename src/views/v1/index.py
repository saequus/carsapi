from django.http import HttpResponse


def view(_):
    template = """
    <html>
        <head>
            <link rel="preconnect" href="https://fonts.googleapis.com">
            <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
            <link href="https://fonts.googleapis.com/css2?family=Poppins&display=swap" rel="stylesheet">
        </head>
        <body>
            <div style='font-family: "Poppins", sans-serif; font-size: 20px; display: flex; justify-content: center;'>
                <div style='display: flex; flex-direction: column; margin: auto;'>
                    <h2>Cars API</h2>
                    <div>
                        <a href='/redoc/'>Swagger</a>
                        <p>
                        <a href='https://github.com/saequus/carsapi#readme'>README</a>
                        <p>
                        <a href='https://github.com/saequus/carsapi'>Repository</a>
                    </div>
                </div>
            </div>
        </body>
    </html>
    """
    return HttpResponse(template)
