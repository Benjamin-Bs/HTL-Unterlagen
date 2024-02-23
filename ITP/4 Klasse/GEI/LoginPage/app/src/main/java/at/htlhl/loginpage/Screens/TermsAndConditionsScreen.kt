package at.htlhl.loginpage.Screens;

import androidx.compose.foundation.background
import androidx.compose.foundation.layout.fillMaxSize
import androidx.compose.foundation.layout.padding
import androidx.compose.material3.Surface
import androidx.compose.runtime.Composable;
import androidx.compose.ui.Modifier
import androidx.compose.ui.graphics.Color
import androidx.compose.ui.res.stringResource
import androidx.compose.ui.tooling.preview.Preview
import androidx.compose.ui.unit.dp
import at.htlhl.loginpage.Components.HeadingTextComponent
import at.htlhl.loginpage.Components.NormalTextComponent
import at.htlhl.loginpage.R
import at.htlhl.loginpage.app.PushProFi
import at.htlhl.loginpage.navigation.PushProFiAppRouter
import at.htlhl.loginpage.navigation.Screen
import at.htlhl.loginpage.navigation.SystemBackButtonHandler

@Composable
fun TermsAndConditionsScreen() {
    Surface(
        modifier = Modifier
            .fillMaxSize()
            .background(color = Color.White)
            .padding(16.dp)
    ) {
        HeadingTextComponent(value = stringResource(id = R.string.terms_and_conditions_heading))
    }

    SystemBackButtonHandler {
        PushProFiAppRouter.navigateTo(Screen.SignUpScreen)
    }
}

@Preview
@Composable
fun TermsAndConditionsScreenPreview(){
    TermsAndConditionsScreen()
}