package at.htlhl.loginpage.app

import androidx.compose.animation.Crossfade
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import at.htlhl.loginpage.Screens.SignUpScreen
import at.htlhl.loginpage.Screens.TermsAndConditionsScreen
import at.htlhl.loginpage.navigation.PushProFiAppRouter
import at.htlhl.loginpage.navigation.Screen

@Composable
fun PushProFi() {
    Surface(
        modifier = Modifier.fillMaxSize(),
        color = Color.White
    ) {

        Crossfade(targetState = PushProFiAppRouter.currentScreen, label = "") { currentState ->
            when (currentState.value) {
                is Screen.SignUpScreen -> {
                    SignUpScreen()
                }
                is Screen.TermsAndConditionsScreen -> {
                    TermsAndConditionsScreen()
                }
            }

        }

    }
}