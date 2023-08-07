from django.db import models
from django.conf import settings
from django.contrib.auth.models import User, AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator
# Create your models here.

class CustomUserManager(BaseUserManager):
    def create_user(self, email, username, password=None):
        if not email:
            raise ValueError('Ingresa un email')
        if not username:
            raise ValueError('Ingresa un nombre de usuario')
        user = self.model(
            email = self.normalize_email(email),
            username=username,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser(self, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            password=password,
        )
        user.is_admin = True
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user

class Usuario(AbstractBaseUser):
    email = models.EmailField(db_index=True, unique=True, max_length=254)
    username = models.CharField(max_length=30, unique=True)
    is_staff = models.BooleanField(default=False)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_superuser = models.BooleanField(default=False)

    objects = CustomUserManager() 

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True
 

class obra(models.Model):
    nombre = models.CharField(max_length=150)
    historia = models.TextField()
    descripcion = models.TextField()
    precio = models.IntegerField(validators=[MaxValueValidator(999999999999)])
    tecnica = models.CharField(max_length=150)
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='static/imagenes/obras/', null=True)

    def __str__(self):
        return self.nombre
    
    @property
    def imagenURL(self):
        try:
            url = self.imagen.url
        except:
            url = ''
        return url
    
class cliente(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=200, null=True)
    email  = models.CharField(max_length=200, null=True)
    
    def __str__(self):
        return self.nombre
    
class carrito(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.SET_NULL, blank=True, null=True)
    fecha_orden = models.DateTimeField(auto_now_add=True)
    completado  = models.BooleanField(default=False, null=True, blank=False)
    id = models.CharField(max_length=200, primary_key=True)

    def __str__(self):
        return str(self.id)

    @property 
    def get_cart_total(self):
        orderitems = self.productocarrito_set.all()
        print(orderitems)
        total = sum([item.get_total for item in orderitems])
        return total
    
    @property 
    def get_cart_items(self):
        orderitems = self.productocarrito_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    
class productocarrito(models.Model):
    producto = models.ForeignKey(obra, on_delete=models.SET_NULL, blank=True, null=True)
    orden = models.ForeignKey(carrito, on_delete=models.SET_NULL, blank=True, null=True)
    quantity = models.IntegerField(default=0, null=True, blank=True)
    fecha_añadido = models.DateTimeField(auto_now_add=True)

    @property 
    def get_total(self):
        total = self.producto.precio * self.quantity
        return total
    

class direccionentrega(models.Model):
    cliente = models.ForeignKey(cliente, on_delete=models.SET_NULL, blank=True, null=True)
    carrito = models.ForeignKey(carrito, on_delete=models.SET_NULL, blank=True, null=True)
    direccion = models.CharField(max_length=200, null=True)
    ciudad = models.CharField(max_length=200, null=True)
    region = models.CharField(max_length=200, null=True)
    codigopostal = models.CharField(max_length=200, null=True)
    fecha_añadido = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.direccion