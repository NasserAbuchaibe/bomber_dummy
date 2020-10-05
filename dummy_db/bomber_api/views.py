from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ParentSerializer, StudentSerializer
from .models import Parent, Student

# Create your views here.

# viewsets for Parent
class ParentView(APIView):
    
    def post(self, request):
        credentials = request.data.get('credentials')
        dict_credentials = credentials[0]
        user_name = dict_credentials["name"]
        password_u = dict_credentials["password"]
        

        try:
            queryset_parent = (Parent.objects.filter(user_name=user_name).filter(password=password_u))
        
            
            for data in queryset_parent:
                id_parent = data.id
            
            queryset_student = Student.objects.filter(parent_id=id_parent)
            serializer_class = StudentSerializer(queryset_student, many=True, context={'request': request})

        except:
            return Response({"Status": "Authentication Failure"})
                   
        return Response (serializer_class.data)
        
