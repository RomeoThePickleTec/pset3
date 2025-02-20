from abc import ABC, abstractmethod

"""
Gestión de Notificaciones
Descripción:
Este proyecto permite enviar notificaciones por diferentes medios (correo electrónico y SMS) sin acoplarse a una implementación específica. Utiliza el Principio de Responsabilidad Única (SRP) y el Principio de Inversión de Dependencias (DIP) para asegurar que la lógica de notificación y el servicio que la usa estén desacoplados.

Principios SOLID aplicados:
✔ SRP: Cada clase tiene una única responsabilidad (Notificación y Servicio de Notificación).
✔ DIP: El servicio depende de una abstracción (Notification) y no de clases concretas (EmailNotification, SMSNotification).

Beneficio: Es fácil agregar nuevos tipos de notificación sin modificar el servicio principal.
"""


class Notification(ABC):
    @abstractmethod
    def send(self, message: str, target: str) -> None:
        pass


class EmailNotification(Notification):
    def send(self, message: str, target: str) -> None:
        print(f"Sending email: {message}\n To: {target}")


class SMSNotification(Notification):
    def send(self, message: str, target: str) -> None:
        print(f"Sending SMS: {message}\n To: {target}")


class CommunicationSystem(ABC):
    @abstractmethod
    def send(self, message: str, target: str) -> None:
        pass


class NotificationSystem(CommunicationSystem):
    def __init__(self, notification: Notification):
        self.notification = notification

    def send(self, message: str, target: str) -> None:
        print('Obtain information to send notification')
        print('Saving log of notification')
        self.notification.send(message, target)


def main():
    email = EmailNotification()
    sms = SMSNotification()

    notification_system = NotificationSystem(sms)
    notification_system.send('Hello World!', '6145542247')


if __name__ == '__main__':
    main()
