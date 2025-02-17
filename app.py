from flask import Flask, render_template, request
import ipaddress

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        try:
            red = request.form["red"]
            red_obj = ipaddress.IPv4Network(red, strict=False)
            
            # Cálculo de subnetting
            num_hosts = (2 ** (32 - red_obj.prefixlen)) - 2
            num_subnets = 2 ** (red_obj.prefixlen - red_obj.network_address.max_prefixlen)

            # Generar subredes
            subredes = list(red_obj.subnets())

            resultado = {
                "red": red,
                "num_hosts": num_hosts,
                "num_subnets": num_subnets,
                "subredes": subredes[:5]  # Mostrar solo las primeras 5 subredes
            }
        except Exception as e:
            resultado = {"error": f"Entrada inválida: {str(e)}"}

    return render_template("index.html", resultado=resultado)

if __name__ == "__main__":
    app.run(debug=True)
