def perform_update_change_request(data, request_change):
    decision = data.get("decision")
    message = data.get("message")

    if decision == "Accepted":
        item_to_change = request_change.item
        new_data = request_change.data
        item_to_change.update(**new_data)

    request_change.status = decision
    request_change.message = message
    request_change.save()
