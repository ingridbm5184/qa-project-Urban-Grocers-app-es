import sender_stand_request
import data

# Función para obtener el cuerpo del kit con un nombre específico
def get_kit_body(name):
    current_user_body = data.kit_body.copy()
    current_user_body["name"] = name
    return current_user_body

# Funciones assert positivas
def positive_assert(kit_body):
    kit_response = sender_stand_request.post_new_kit(kit_body)
    assert kit_response.status_code == 201
    assert kit_response.json()['name'] == kit_body['name']

# Funciones assert negativas
def negative_assert(kit_body):
    kit_response = sender_stand_request.post_new_kit(kit_body)
    assert kit_response.status_code == 400

    # TEST
# Test 1: nombre con 1 carácter
    def test_kit_name_minimum_characters():
        kit_body = get_kit_body("a")
        # Pasar auth_token a la función de aserción
        positive_assert(kit_body)

# Test 2: número permitido de caracteres (511)
def test_kit_name_maximum_characters():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")
    positive_assert(kit_body)

# Test 3: número de caracteres es menor que la cantidad permitida (0)
def test_kit_name_below_minimum_characters():
    kit_body = get_kit_body("")
    negative_assert(kit_body)

# Test 4: número de caracteres es mayor que la cantidad permitida (512)
def test_kit_name_above_maximum_characters():
    kit_body = get_kit_body("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")
    negative_assert(kit_body)

# Test 5: se permiten caracteres especiales
def test_kit_name_special_characters():
    kit_body = get_kit_body("$@/&%$")
    positive_assert(kit_body)

# Test 6: se permiten espacios
def test_kit_name_with_spaces():
    kit_body = get_kit_body(" A Aaa ")
    positive_assert(kit_body)

# Test 7: se permiten números
def test_kit_name_as_number_allowed():
    kit_body = get_kit_body(123)
    positive_assert(kit_body)

# Test 8: sin caracteres
def test_create_kit_no_name_get_error_response():
    kit_body = data.kit_body.copy()
    kit_body.pop("name")
    negative_assert(kit_body)

# Test 9: no se permiten números
def test_kit_name_as_number_rejected():
    kit_body = get_kit_body(123)
    negative_assert(kit_body)


