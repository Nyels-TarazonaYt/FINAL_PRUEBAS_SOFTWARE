from flask import Flask, render_template, jsonify
import app
app = Flask(__name__)

productos = {
    1: {'nombre': 'Camisa', 'precio': 20.00},
    2: {'nombre': 'Pantalones', 'precio': 25.00},
    # Agrega más productos según sea necesario
}

@app.route('/producto/<int:producto_id>')
def detalle_producto(producto_id):
    producto = productos.get(producto_id)
    if producto:
        return render_template('detalle_producto.html', producto=producto)
    else:
        return "Producto no encontrado", 404

@app.route('/')
def lista_productos():
    return render_template('lista_productos.html', productos=productos)

if __name__ == '__main__':
    app.run(debug=True)
