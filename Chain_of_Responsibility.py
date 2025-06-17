class Request:
    def __init__(self, student_name, request_type, details):
        self.student_name = student_name
        self.request_type = request_type  # for example "extra_exam", "fee_reduction", ...
        self.details = details


class Approver:
    def __init__(self, next_approver=None):
        self.next_approver = next_approver

    def handle_request(self, request):
        # Base handler does nothing, just passes along
        if self.next_approver:
            return self.next_approver.handle_request(request)
        else:
            # In case of unhandled requests
            print(f"Request from {request.student_name} for '{request.request_type}' could not be handled.")
            return False


# Concrete handlers
class Mentor(Approver):
    def handle_request(self, request):
        if request.request_type == "extension" and request.details.get("days") <= 3:
            print(f"Mentor approved extension of {request.details.get('days')} days for {request.student_name}.")
            return True
        else:
            print(f"Mentor cannot handle request '{request.request_type}' — passing to next approver.")
            return super().handle_request(request)


class HeadOfDepartment(Approver):
    def handle_request(self, request):
        if request.request_type == "extra_exam":
            print(f"Head of Department approved extra exam attempt for {request.student_name}.")
            return True
        elif request.request_type == "extension" and request.details.get("days") <= 7:
            print(f"Head of Department approved extension of {request.details.get('days')} days for {request.student_name}.")
            return True
        else:
            print(f"Head of Department cannot handle request '{request.request_type}' — passing to next approver.")
            return super().handle_request(request)


class Dean(Approver):
    def handle_request(self, request):
        if request.request_type == "fee_reduction":
            print(f"Dean approved fee reduction for {request.student_name}.")
            return True
        elif request.request_type == "extension":
            print(f"Dean approved extension of {request.details.get('days')} days for {request.student_name}.")
            return True
        else:
            print(f"Dean cannot handle request '{request.request_type}'.")
            return super().handle_request(request)


class Rector(Approver):
    def handle_request(self, request):
        if request.request_type == "exchange_exception":
            print(f"Rector approved exchange exception for {request.student_name}.")
            return True
        else:
            print(f"Rector cannot handle request '{request.request_type}' — no further approvers.")
            return super().handle_request(request)



# Example usage
if __name__ == "__main__":
    # Create the chain: Mentor -> Head -> Dean ->Rector
    rector = Rector()   # No next approver
    dean = Dean(next_approver=rector)
    head = HeadOfDepartment(next_approver=dean)
    mentor = Mentor(next_approver=head)

    # Example requests
    r1 = Request("Alice", "extension", {"days": 2})
    r2 = Request("Bob", "extra_exam", {})
    r3 = Request("Lea", "fee_reduction", {"percent": 50})
    r4 = Request("Aram", "extension", {"days": 10})
    r5 = Request("David", "unknown_request", {})
    r6 = Request("Sam", "exchange_exception", {})

    # Process requests
    mentor.handle_request(r1)
    print("-----")
    mentor.handle_request(r2)
    print("-----")
    mentor.handle_request(r3)
    print("-----")
    mentor.handle_request(r4)
    print("-----")
    mentor.handle_request(r5)
    print("-----")
    mentor.handle_request(r6)