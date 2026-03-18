def register_client(clients_dict, client_id, first_name, last_name, email):
    if client_id in clients_dict:
        return clients_dict, "Client already exists"

    clients_dict[client_id] = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email
    }

    return clients_dict, "Client registered successfully"


def view_clients(clients_dict):
    if not clients_dict:
        return "No clients registered"

    result = "\n--- CLIENT LIST ---\n"

    for client_id in clients_dict:
        client = clients_dict[client_id]
        full_name = client["first_name"] + " " + client["last_name"]

        result += f"ID: {client_id} | Name: {full_name} | Email: {client['email']}\n"

    return result