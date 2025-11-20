from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.

class Message(models.Model):
    """
    Model for storing message board messages
    """
    title = models.CharField(max_length=200, help_text="Message title")
    content = models.TextField(help_text="Message content")
    author = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name='board_messages',
        help_text="Message author"
    )
    created_at = models.DateTimeField(
        default=timezone.now,
        help_text="When the message was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        help_text="When the message was last updated"
    )
    is_active = models.BooleanField(
        default=True,
        help_text="Whether the message is active/visible"
    )
    
    class Meta:
        ordering = ['-created_at']  # Newest messages first
        verbose_name = "Message"
        verbose_name_plural = "Messages"
        
    def __str__(self):
        return f"{self.title} by {self.author.username}"
        
    def get_absolute_url(self):
        from django.urls import reverse
        return reverse('message_detail', kwargs={'pk': self.pk})
