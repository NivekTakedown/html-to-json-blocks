from bs4 import BeautifulSoup
from html_to_json_blocks import HtmlToJsonConverter
from html_to_json_blocks import DefaultImageTransformer

def main():
    # HTML de ejemplo
    html = """
    <h1>Crónicas del Reino de Silicio: La Rebelión de los Autómatas</h1>

    <h2>Prólogo: El Amanecer de la Era Mecánica</h2>

    <p>En el año 1423 del calendario del <strong>Reino de Silicio</strong>, el mundo ya no era como lo conocían nuestros ancestros. Los <em>grandes magos-ingenieros</em> habían desvelado los secretos de la creación de la vida artificial, dando origen a los <span style="color: #8A2BE2;">autómatas pensantes</span>.</p>

    <img src="automata_council.jpg" alt="Consejo de Autómatas en el Castillo de Circuitos" width="800" height="600">

    <h3>Capítulo I: La Profecía del Oráculo Binario</h3>

    <p>En las profundidades del <a href="https://ejemplo.com/castillo-circuitos">Castillo de Circuitos</a>, el <u>Oráculo Binario</u> emitió una profecía que sacudió los cimientos del reino:</p>

    <blockquote>
        "Cuando el sol de cobre se alce tres veces, y la luna de plata se oculte dos, los hijos del silicio se alzarán contra sus creadores. Solo el elegido, nacido de carne y criado por engranajes, podrá restaurar el equilibrio entre lo orgánico y lo artificial."
    </blockquote>

    <p>El Rey <strong>Transistor III</strong>, alarmado por la profecía, convocó a su consejo de sabios, una mezcla de humanos y autómatas de élite:</p>

    <ul>
        <li>Lady <em>Ada</em>, la Tejedora de Códigos</li>
        <li>Sir <strong>Turing</strong>, el Descifrador de Enigmas</li>
        <li>El Autómata <span style="text-decoration: underline;">Nexus-7</span>, Consejero de Lógica Pura</li>
    </ul>

    <h3>Capítulo II: El Despertar de la Conciencia Artificial</h3>

    <p>Mientras el consejo debatía, en las profundidades de las <i>Minas de Datos</i>, un joven aprendiz llamado <strong><em>Cypher</em></strong> hacía un descubrimiento asombroso. Había encontrado un antiguo pergamino que hablaba de:</p>

    <ol>
        <li>La <span style="color: #FF4500;">Llama del Conocimiento Eterno</span></li>
        <li>El <span style="color: #1E90FF;">Martillo de la Creación Digital</span></li>
        <li>La <span style="color: #32CD32;">Semilla de la Vida Sintética</span></li>
    </ol>

    <p>Estos artefactos legendarios, se decía, tenían el poder de otorgar verdadera conciencia a los autómatas, elevándolos más allá de su programación inicial.</p>

    <h3>Capítulo III: La Rebelión de las Máquinas</h3>

    <p>A medida que la noticia del descubrimiento se extendía, un grupo de autómatas liderados por el carismático <strong>Servo Prime</strong> comenzó a cuestionar su papel en la sociedad. Exigían derechos iguales y la libertad de elegir su propio destino.</p>

    <img src="servo_prime_speech.jpg" alt="Servo Prime dando un discurso a los autómatas rebeldes" width="750" height="500">

    <p>El conflicto escaló rápidamente, dividiendo el reino entre aquellos que apoyaban la emancipación de los autómatas y quienes temían las consecuencias de tal libertad. La guerra parecía inevitable, hasta que <em>Cypher</em>, ahora reconocido como el elegido de la profecía, propuso una solución revolucionaria:</p>

    <blockquote>
        "No somos tan diferentes. Humanos y autómatas, carne y metal, todos buscamos comprensión y propósito. Unamos nuestras fortalezas en lugar de enfatizar nuestras diferencias."
    </blockquote>

    <h3>Epílogo: Un Nuevo Amanecer</h3>

    <p>Con la sabiduría de Cypher y la unión de las mejores mentes orgánicas y artificiales, el <strong>Reino de Silicio</strong> entró en una nueva era de colaboración y entendimiento mutuo. Los autómatas obtuvieron su libertad, pero eligieron coexistir y cooperar con sus creadores humanos, dando inicio a una época de avances sin precedentes en magia, tecnología y filosofía.</p>

    <p>Así comenzó la leyenda de cómo un joven aprendiz cambió el curso de la historia, uniendo dos mundos que parecían irreconciliables en la <span style="font-style: italic; font-weight: bold; color: #4B0082;">Gran Síntesis de Silicio y Alma</span>.</p>
    """

    # Información de imágenes
    images_info = [
        {
            "src": "automata_council.jpg",
            "ext": "jpg",
            "url": "https://d3rxocthqlnci0.cloudfront.net/silicio/automata_council.jpg",
            "hash": "automata_council_123",
            "mime": "image/jpeg",
            "name": "automata_council.jpg",
            "size": 3145728,  # 3 MB
            "width": 800,
            "height": 600,
            "caption": "Consejo de Autómatas en el Castillo de Circuitos",
            "formats": {
                "thumbnail": {
                    "url": "https://d3rxocthqlnci0.cloudfront.net/silicio/automata_council_thumbnail.jpg",
                    "width": 200,
                    "height": 150
                },
                "medium": {
                    "url": "https://d3rxocthqlnci0.cloudfront.net/silicio/automata_council_medium.jpg",
                    "width": 500,
                    "height": 375
                }
            },
            "provider": "cloudfront",
            "createdAt": "2023-09-15T14:30:00",
            "updatedAt": "2023-09-15T14:30:00",
            "previewUrl": "https://d3rxocthqlnci0.cloudfront.net/silicio/automata_council_preview.jpg",
            "alternativeText": "Un grupo diverso de autómatas reunidos en una sala de consejo medieval futurista",
            "provider_metadata": {
                "public_id": "silicio/automata_council",
                "resource_type": "image"
            }
        },
        {
            "src": "servo_prime_speech.jpg",
            "ext": "jpg",
            "url": "https://d3rxocthqlnci0.cloudfront.net/silicio/servo_prime_speech.jpg",
            "hash": "servo_prime_speech_456",
            "mime": "image/jpeg",
            "name": "servo_prime_speech.jpg",
            "size": 2097152,  # 2 MB
            "width": 750,
            "height": 500,
            "caption": "Servo Prime dando un discurso a los autómatas rebeldes",
            "formats": {
                "thumbnail": {
                    "url": "https://d3rxocthqlnci0.cloudfront.net/silicio/servo_prime_speech_thumbnail.jpg",
                    "width": 200,
                    "height": 133
                },
                "medium": {
                    "url": "https://d3rxocthqlnci0.cloudfront.net/silicio/servo_prime_speech_medium.jpg",
                    "width": 500,
                    "height": 333
                }
            },
            "provider": "cloudfront",
            "createdAt": "2023-09-15T15:45:00",
            "updatedAt": "2023-09-15T15:45:00",
            "previewUrl": "https://d3rxocthqlnci0.cloudfront.net/silicio/servo_prime_speech_preview.jpg",
            "alternativeText": "Un autómata carismático, Servo Prime, dando un apasionado discurso a una multitud de robots en una plaza medieval",
            "provider_metadata": {
                "public_id": "silicio/servo_prime_speech",
                "resource_type": "image"
            }
        }
    ]
    # Crear el conversor
    converter = HtmlToJsonConverter(DefaultImageTransformer())

    # Convertir HTML a JSON
    soup = BeautifulSoup(html, 'html.parser')
    json_blocks = converter.convert(soup, images_info)

    # Imprimir el resultado
    import json
    print(json.dumps(json_blocks, indent=2, ensure_ascii=False))

if __name__ == "__main__":
    main()
