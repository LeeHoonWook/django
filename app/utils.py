from rest_framework.response import Response


def MsgOk(status: int = 200):
    return Response({"msg": "ok"}, status=status)
