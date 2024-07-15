from config import app, db
import views
import model

# Eseguire l'app Flask
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # Crea tutte le tabelle
    app.run(debug=True)
