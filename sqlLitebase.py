{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9c06943a",
   "metadata": {},
   "outputs": [],
   "source": [
    "app = Flask(__name__)\n",
    "app.secret_key = \"secret_key\"\n",
    "app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///users.db'\n",
    "app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False\n",
    "db = SQLAlchemy(app)\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.9.13"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
